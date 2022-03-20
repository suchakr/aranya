#!/bin/bash
cd imgs
echo `pwd`

#for f in ../../data\~/opensource_vikarabad_amarabad_mixed_train_data1/nofire/* ; do f2=${f/.*\//\./} ; ln -s $f ${f2/.jpg/_nofire.jpg};  done
#for f in ../../data\~/opensource_vikarabad_amarabad_mixed_train_data1/fire/* ; do f2=${f/.*\//\./} ; ln -s $f ${f2/.jpg/_fire.jpg};  done


ls *jpg | grep _fire | grep -v ^fire | perl -lne 'print qq($_,) , /_fire/ ? qq(FIRE) : qq(NOFIRE)' | shuf > aa_fire_arff.data
ls *jpg | grep _nofire | grep -v ^nofire | perl -lne 'print qq($_,) , /_fire/ ? qq(FIRE) : qq(NOFIRE)' | shuf > aa_nofire_arff.data

TRAIN=aa_train_300_250.arff
rm $TRAIN
cp aa_arff.skel $TRAIN
cat aa_fire_arff.data |  head -300 >> $TRAIN
cat aa_nofire_arff.data | head -250 >>$TRAIN

head -10 $TRAIN
TEST=aa_test_185_185.arff
rm $TEST
cp aa_arff.skel $TEST
cat aa_fire_arff.data |  tail -185 >> $TEST
cat aa_nofire_arff.data | head -185 >>$TEST

cd ..

# weka.classifiers.meta.FilteredClassifier -F "weka.filters.unsupervised.instance.imagefilter.BinaryPatternsPyramidFilter -D /Users/sunder/projects/aranya/agni/imgs" -S 1 -W weka.classifiers.meta.AutoWEKAClassifier -- -seed 123 -timeLimit 5 -memLimit 1024 -nBestConfigs 1 -metric errorRate -parallelRuns 4
