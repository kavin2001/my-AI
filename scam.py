import argparse
import json
import os
import time

try:
    import requests
except ImportError:
    raise ImportError("This script requires the requests package to work. Install it using 'pip install requests'")


def scan(url_batch, api_key):
  url = 'https://www.virustotal.com/vtapi/v2/url/scan'
  scan_id_list = []
  for URL in url_batch:
    try:
      params = {'apikey': api_key, 'url': URL }
      response = requests.post(url, data=params)
      scan_id_list.append(response.json()['scan_id'])
    except ValueError as e:
      print ("Rate limit detected:"), e
      continue
    except Exception:
      print ("Error detected:")
      continue
  return scan_id_list

def report(scan_id_list, api_key):
  url = 'https://www.virustotal.com/vtapi/v2/url/report'
  report_list = []
  for id in scan_id_list:
    try:
      params = {'apikey': api_key, 'resource': id }
      response = requests.get(url, params=params)
      report_list.append(response.json())
    except ValueError as e:
      print ("Rate limit detected:"), e
      continue
    except Exception:
      print ("Error detected:")
      continue
  return report_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('link_fp', help="path to the links you want to scan")
    parser.add_argument('output_fp', help="path to your output file")
    parser.add_argument('response_fp', help='path to the response file you want to store')
    parser.add_argument('api_key', help='virustotal API key')
    args = parser.parse_args()

    url_list = []
    output_file = open(args.output_fp, 'a')
    response_file = open(args.response_fp, 'a')
    with open(args.link_file) as f:
        for line in f:
            url_list.append(line.rstrip())
        response = []
        report_list = []
        for i in xrange(len(url_list)):
            if i%4 == 0:
                # API cooldown time is 60 seconds
                time.sleep(60)
                url_batch = []
            url_batch.append(url_list[i])
            if i%4 == 3 or i == len(url_list)-1:
                response += scan(url_batch)
                response_file.write('\n'.join(str(t) for t in response))
    print ('scan complete''')
    for i in xrange(len(response)):
        if i%4 == 0:
            time.sleep(60)
            scan_list = []
        scan_list.append(response[i])
        if (i%4 == 3 or i == len(response)-1):
            reportBatch = report(scan_list)
            report_list += reportBatch
            for r in reportBatch:
                json.dump(r , output_file)
                output_file.write("\n")
    output_file.close()
    response_file.close()


if __name__ == '__main__':
    main() 