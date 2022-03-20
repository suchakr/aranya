all: imgattrs nofilename j48

imgattrs : bppf
nofilename : bppf_nofn

bppf: aa_tt_02_img_bppf.arff aa_vv_02_img_bppf.arff
bppf_nofn: aa_tt_03_bppf_nofn.arff aa_vv_03_bppf_nofn.arff
j48: aa_tt_04_img_bppf_j48.model aa_tt_04_img_bppf_j48_vv_preds.csv 

%02_img_bppf.arff :  %01.arff 
	time java weka.Run .BinaryPatternsPyramidFilter \
	 -D /Users/sunder/projects/aranya/agni/imgs \
	 -i $< -o $@  

%03_bppf_nofn.arff :  %02_img_bppf.arff 
	time java weka.Run .RemoveByName -E filename -i $< -o  $@

aa_tt_04_img_bppf_j48.model : aa_tt_03_bppf_nofn.arff 
	time java weka.Run .J48 -t $< \
		-T $(subst _tt_,_vv_,$<) \
		-d $@ \
		>  $(subst .model,.modelinfo,$@) 

%_vv_preds.csv : %.model
	time java weka.Run .J48 \
		-classifications ".CSV -file ~$@" \
		-l $< \
		-T aa_vv_03_bppf_nofn.arff
	echo "id,filename" > ~fn.csv
	grep jpg aa_vv_02_img_bppf.arff  | cut -d, -f1 | cat -n | perl  -lpe 's/^\D+//; s/\s+/,/' >> ~fn.csv	 
	paste -d, ~fn.csv ~$@ | grep ... > $@
	rm ~*csv
