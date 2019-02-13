# Demarrage de Hadoop
sbin/.start-all.sh

# Creation d'un dossier sur HDFS
hadoop fs -mkdir /data

# Copie de notre dataset vers HDFS
bin/hadoop fs -put ~/dataset.csv /data/dataset.csv

# Arret de Hadoop
sbin/.stop-all.sh
