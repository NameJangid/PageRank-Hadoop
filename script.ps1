hadoop fs -mkdir /input
hadoop fs -put C:\Users\Manuj\Desktop\python\input.txt /input
hadoop fs -rm -r /output1
hadoop jar C:\hadoop-2.8.0\share\hadoop\tools\lib\hadoop-streaming-2.8.0.jar -file C:\Users\Manuj\Desktop\python\map1.py -mapper "python C:\Users\Manuj\Desktop\python\map1.py" -file C:\Users\Manuj\Desktop\python\red1.py -reducer "python C:\Users\Manuj\Desktop\python\red1.py 8" -numReduceTasks 1 -input /input/* -output /output1
hadoop fs -rm -r /output2
hadoop jar C:\hadoop-2.8.0\share\hadoop\tools\lib\hadoop-streaming-2.8.0.jar -file C:\Users\Manuj\Desktop\python\map2.py -mapper "python C:\Users\Manuj\Desktop\python\map2.py" -file C:\Users\Manuj\Desktop\python\red2.py -reducer "python C:\Users\Manuj\Desktop\python\red2.py 8" -numReduceTasks 1 -input /output1/* -output /output2

For ($i=0; $i -lt 8; $i++) {
    echo "
    
    ----$i----
    
    "
hadoop fs -rm -r /output3
hadoop jar C:\hadoop-2.8.0\share\hadoop\tools\lib\hadoop-streaming-2.8.0.jar -file C:\Users\Manuj\Desktop\python\map3.py -mapper "python C:\Users\Manuj\Desktop\python\map3.py 8 C:\Users\Manuj\Desktop\python\out.txt " -file C:\Users\Manuj\Desktop\python\red2.py -reducer "python C:\Users\Manuj\Desktop\python\red3.py" -numReduceTasks 1 -input /output2/* -output /output3
hadoop fs -get /output3/* C:\Users\Manuj\Desktop\python\out
rm C:\Users\Manuj\Desktop\python\out.txt
mv C:\Users\Manuj\Desktop\python\out\part* C:\Users\Manuj\Desktop\python\out.txt
rm C:\Users\Manuj\Desktop\python\out\*CESS
rm C:\Users\Manuj\Desktop\python\out\part*


hadoop fs -rm -r /output3



}