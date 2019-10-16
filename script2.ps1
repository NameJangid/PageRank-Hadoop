hadoop fs -mkdir /input2
hadoop fs -put C:\Users\Manuj\Desktop\python\input2.txt /input2
hadoop fs -rm -r /output1
hadoop jar C:\hadoop-2.8.0\share\hadoop\tools\lib\hadoop-streaming-2.8.0.jar -file C:\Users\Manuj\Desktop\python\map1.py -mapper "python C:\Users\Manuj\Desktop\python\map1.py" -file C:\Users\Manuj\Desktop\python\red1.py -reducer "python C:\Users\Manuj\Desktop\python\red1.py 500" -numReduceTasks 1 -input /input2/* -output /output1
hadoop fs -rm -r /output2
hadoop jar C:\hadoop-2.8.0\share\hadoop\tools\lib\hadoop-streaming-2.8.0.jar -file C:\Users\Manuj\Desktop\python\map2.py -mapper "python C:\Users\Manuj\Desktop\python\map2.py" -file C:\Users\Manuj\Desktop\python\red2.py -reducer "python C:\Users\Manuj\Desktop\python\red2.py 500" -numReduceTasks 1 -input /output1/* -output /output2

For ($i=0; $i -lt 10; $i++) {
    echo "
    
    ----$i----
    
    "
hadoop fs -rm -r /output3
hadoop jar C:\hadoop-2.8.0\share\hadoop\tools\lib\hadoop-streaming-2.8.0.jar -file C:\Users\Manuj\Desktop\python\map3.py -mapper "python C:\Users\Manuj\Desktop\python\map3.py 500 C:\Users\Manuj\Desktop\python\out2.txt " -file C:\Users\Manuj\Desktop\python\red2.py -reducer "python C:\Users\Manuj\Desktop\python\red3.py" -numReduceTasks 1 -input /output2/* -output /output3
hadoop fs -get /output3/* C:\Users\Manuj\Desktop\python\out
rm C:\Users\Manuj\Desktop\python\out2.txt
mv C:\Users\Manuj\Desktop\python\out\part* C:\Users\Manuj\Desktop\python\out2.txt
rm C:\Users\Manuj\Desktop\python\out\*CESS
rm C:\Users\Manuj\Desktop\python\out\part*


hadoop fs -rm -r /output3



}