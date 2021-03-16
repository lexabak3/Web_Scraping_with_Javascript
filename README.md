# Parsing web site that uses a Javascript
brute parsing site with selenium, bs4, requests_html

Log example:
```
Parse main page...
Final count of elements - 2076
Find links on main page
Loading html snippets from links...
 21%|██▏       | 445/2076 [36:29<2:18:05,  5.08s/it]('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
 27%|██▋       | 569/2076 [46:59<2:20:07,  5.58s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 30%|███       | 623/2076 [51:39<2:01:31,  5.02s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 30%|███       | 632/2076 [52:34<2:02:23,  5.09s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 31%|███▏      | 649/2076 [54:11<2:00:01,  5.05s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 33%|███▎      | 677/2076 [56:40<1:55:33,  4.96s/it]net::ERR_CONNECTION_REFUSED 
 34%|███▎      | 698/2076 [58:55<2:08:15,  5.58s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 36%|███▌      | 737/2076 [1:02:33<1:54:39,  5.14s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 36%|███▌      | 740/2076 [1:02:58<2:23:40,  6.45s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 38%|███▊      | 797/2076 [1:09:57<1:45:23,  4.94s/it]net::ERR_CONNECTION_REFUSED
 38%|███▊      | 799/2076 [1:10:40<4:09:52, 11.74s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 40%|███▉      | 822/2076 [1:12:44<1:42:56,  4.93s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 41%|████      | 842/2076 [1:14:32<1:41:14,  4.92s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 41%|████      | 843/2076 [1:14:50<3:00:41,  8.79s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 42%|████▏     | 868/2076 [1:17:06<1:45:45,  5.25s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 43%|████▎     | 891/2076 [1:19:27<1:56:51,  5.92s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 46%|████▌     | 948/2076 [1:24:23<1:36:32,  5.14s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 46%|████▌     | 949/2076 [1:24:39<2:37:40,  8.39s/it]('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
 46%|████▌     | 955/2076 [1:25:23<2:00:23,  6.44s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 50%|████▉     | 1032/2076 [1:32:15<1:31:11,  5.24s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 52%|█████▏    | 1081/2076 [1:36:30<1:22:33,  4.98s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 53%|█████▎    | 1097/2076 [1:38:03<1:29:34,  5.49s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 54%|█████▍    | 1127/2076 [1:40:46<1:18:04,  4.94s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 55%|█████▌    | 1142/2076 [1:42:13<1:17:58,  5.01s/it]net::ERR_CONNECTION_REFUSED 
 56%|█████▋    | 1171/2076 [1:44:58<1:14:09,  4.92s/it]net::ERR_CONNECTION_REFUSED 
 57%|█████▋    | 1175/2076 [1:45:30<1:32:24,  6.15s/it]('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
 58%|█████▊    | 1209/2076 [1:48:30<1:11:27,  4.95s/it]('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
 59%|█████▉    | 1222/2076 [1:49:47<1:11:41,  5.04s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 59%|█████▉    | 1229/2076 [1:50:33<1:15:31,  5.35s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 60%|█████▉    | 1243/2076 [1:51:54<1:10:04,  5.05s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 62%|██████▏   | 1292/2076 [1:56:10<1:07:11,  5.14s/it]('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
 65%|██████▍   | 1340/2076 [2:00:23<1:01:34,  5.02s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 68%|██████▊   | 1411/2076 [2:06:38<59:03,  5.33s/it]net::ERR_CONNECTION_REFUSED
 68%|██████▊   | 1414/2076 [2:07:06<1:16:30,  6.93s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 71%|███████   | 1470/2076 [2:11:58<52:43,  5.22s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 74%|███████▍  | 1539/2076 [2:18:02<47:15,  5.28s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 76%|███████▌  | 1580/2076 [2:21:44<42:06,  5.09s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 76%|███████▋  | 1588/2076 [2:22:35<44:16,  5.44s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 78%|███████▊  | 1620/2076 [2:25:28<38:50,  5.11s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 78%|███████▊  | 1627/2076 [2:26:13<39:53,  5.33s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 80%|████████  | 1668/2076 [2:29:50<35:01,  5.15s/it]HTTPSConnectionPool(host='urbantoronto.ca', port=443)
 84%|████████▍ | 1747/2076 [2:37:07<30:16,  5.52s/it]('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
 84%|████████▍ | 1750/2076 [3:07:51<24:55:27, 275.24s/it]net::ERR_SOCKET_NOT_CONNECTED
100%|██████████| 2076/2076 [3:48:25<00:00,  6.60s/it]
Parsing html tags: picking out the data you are looking for...
Saving data to an Excel table

Process finished with exit code 0
```
