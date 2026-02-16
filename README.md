If you have installed poetry simply run the program using followng command
-> "poetry run python sample.py"

Dataset Info:
<class 'pandas.DataFrame'>
RangeIndex: 4061 entries, 0 to 4060
Data columns (total 10 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   date             4061 non-null   datetime64[us]
 1   totalChallan     4061 non-null   int64
 2   disposedChallan  4061 non-null   int64
 3   pendingChallan   4061 non-null   int64
 4   pendingAmount    4061 non-null   int64
 5   disposedAmount   4061 non-null   int64
 6   totalAmount      4061 non-null   int64
 7   pendingCourt     4061 non-null   int64
 8   disposedCourt    4061 non-null   int64
 9   totalCourt       4061 non-null   int64
dtypes: datetime64[us](1), int64(9)
memory usage: 317.4 KB
None

Integrity Checks:
Amount mismatch rows: 0
Challan mismatch rows: 0
Court mismatch rows: 0

Summary Statistics:
                             date   totalChallan  disposedChallan  \
count                        4061    4061.000000      4061.000000
mean   2020-07-24 10:47:07.874907  102564.295986     39190.895100
min           2015-01-01 00:00:00      10.000000         6.000000
25%           2017-10-12 00:00:00    1864.000000      1032.000000
50%           2020-07-24 00:00:00  104931.000000     47012.000000
75%           2023-05-05 00:00:00  174420.000000     67133.000000
max           2026-12-02 00:00:00  332710.000000     96645.000000
std                           NaN   94274.309905     30766.668065

       pendingChallan  pendingAmount  disposedAmount   totalAmount  \
count     4061.000000   4.061000e+03    4.061000e+03  4.061000e+03
mean     63373.400886   9.998178e+07    5.655994e+07  1.565417e+08
min          3.000000   2.040000e+04    6.700000e+03  5.440000e+04
25%       1131.000000   1.765850e+06    5.127580e+06  7.183220e+06
50%      53038.000000   5.541961e+07    5.496822e+07  1.055297e+08
75%     102064.000000   1.658786e+08    9.343013e+07  2.700863e+08
max     280588.000000   5.659961e+08    2.071116e+09  2.147021e+09
std      69079.820831   1.295082e+08    6.258393e+07  1.719233e+08

        pendingCourt  disposedCourt     totalCourt  disposal_rate  \
count    4061.000000    4061.000000    4061.000000    4061.000000
mean    31538.348190    5563.763113   37102.111303       0.418068
min         0.000000       0.000000       0.000000       0.013523
25%       843.000000     119.000000     945.000000       0.277833
50%     23338.000000    6332.000000   31606.000000       0.424608
75%     54761.000000    9851.000000   65373.000000       0.516539
max    136032.000000   15910.000000  146748.000000       0.931000
std     34442.072462    4879.257000   37600.288253       0.202457

        court_rate      avg_fine  realization_rate  backlog_ratio
count  4061.000000   4061.000000       4061.000000    4061.000000
mean      0.367419   2013.695100          0.449662       2.635436
min       0.000000    262.235142          0.006680       0.074114
25%       0.250584   1153.342725          0.267134       0.935961
50%       0.372206   1502.517825          0.424939       1.355113
75%       0.438404   1872.714034          0.591292       2.599291
max       0.938312  33312.368149          0.964646      72.950617
std       0.187156   1797.270434          0.221314       3.906111

Yearly Growth:
            totalChallan  YoY_growth_%
date
2015-12-31        112492           NaN
2016-12-31        404445    259.532233
2017-12-31        593048     46.632546
2018-12-31       4317842    628.076311
2019-12-31      20628507    377.750390
2020-12-31      41190446     99.677301
2021-12-31      42401371      2.939820
2022-12-31      47649749     12.377850
2023-12-31      67911658     42.522593
2024-12-31      81892378     20.586627
2025-12-31      97884423     19.528124
2026-12-31      11527247    -88.223614

Correlation (Revenue vs Volume):
              totalChallan  totalAmount
totalChallan      1.000000     0.938644
totalAmount       0.938644     1.000000

ADF Test Results:
ADF Statistic: 0.07793030862803313
p-value: 0.9645215880580885
