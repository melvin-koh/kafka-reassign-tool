#!/usr/bin/env python

import argparse, json
import subprocess, sys

KERBEROS = False
TLS = False
ZOOKEEPER_LIST = None
BROKER_LIST = None

def load_properties_file(filepath):
  file = open(filepath, "r")

def retrieve_kafka_properties():
  cmd = "ls -t /var/run/cloudera-scm-agent/process | grep KAFKA_BROKER"
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=None)
  if p.wait() == 0:
    process_dir = "/var/run/cloudera-scm-agent/process/{}".format(p.stdout.read().partition('\n')[0])
  else:
    print("Error: This tool must be run on a Cloudera managed Kafka broker")
    sys.exit(-1)
  load_properties_file("{}/kafka.properties".format(process_dir))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--topic", help="Topic to update. If option is not used, operation will apply to all existing topics")
  parser.add_argument("-r", "--replication-factor", help="Target replication factor", required=True)
  args = parser.parse_args()

  retrieve_kafka_properties()

if __name__ == "__main__":
  main()
