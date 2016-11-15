        2
   1 /bin/bash: 2: command not found
      3 d
      5 #gujie
      6   t='2016-07-26'
      4    6 chujie=('publish_chujie_1810001095_20160726.log' 
        'publish_chujie_1084887800_20160726.log' 
        'publish_chujie_1652741173_20160726.log' 
        'publish_chujie_5779255215_20160726.log'
        'publish_chujie_5779042658_20160726.log' 
        'publish_chujie_5779255215_20160726.log')
      7       7 chujie_uid=publish_info_chujie_uid_${dt}.log
      8       8 chujie_mid_succ=publish_info_chujie_mid_success_${dt}.log
      9    ish_chujie_1652741173_20160726.log' 'publish_chujie_57786        42151_20        160726.log' 'publ   9 chujie_mid_fail=publish_info_chujie_mid_fail_${dt}.log
     10      10 rm ${chujie_uid} ${chujie_mid_succ} ${chujie_mid_fail}
     11      11 for file in ${chujie[@]}
     12      12 do
     13      13     cat $file | grep SUCCESS -B1 | cut -d' ' -f 8 | cut -d $'\t' -f 2 | sort -u >> ${chujie_uid}
     14      14     cat $file | grep SUCCESS -B1 | cut -d' ' -f 8 | cut -d $'\t' -f 1 | sort -u >> ${chujie_mid_succ}
     15      15     cat $file | grep FAILURE -B1 | cut -d' ' -f 8 | cut -d $'\t' -f 1 | sort -u >> ${chujie_mid_fail}
     16      16 done
     17      17 #get daima
     18      18 daima=('publish_chujie_57792548_20160726.log' 'publish_chujie_5779047597_20160726.log')
     19      19 daima_uid=publish_info_daima_uid_${dt}.log
     20      20 daima_mid_succ=publish_info_daima_mid_success_${dt}.log
     21      21 daima_mid_fail=publish_info_daima_mid_fail_${dt}.log
     22      22 rm ${daima_uid} ${daima_mid_succ} ${daima_mid_fail}
     23      23 for file in ${daima[@]}
     24      24 do
     25      25     cat $file | grep SUCCESS -B1 | cut -d' ' -f 8 | cut -d $'\t' -f 2 | sort -u >> ${daima_uid}
     26      26     cat $file | grep SUCCESS -B1 | cut -d' ' -f 8 | cut -d $'\t' -f 1 | sort -u >> ${daima_mid_succ}
     27      27     cat $file | grep FAILURE -B1 | cut -d' ' -f 8 | cut -d $'\t' -f 1 | sort -u >> ${daima_mid_fail}
     28      28 done
     29      29 #get homepage
     30      30 homepage=('publish_chujie_1802431843_20160726.log' 'publish_chujie_2826732292_20160726.log' 'publish_chujie_5287518665_20160726.log')
     31      31 homepage_uid=publish_info_homepage_uid_${dt}.log
     32      32 homepage_mid_succ=publish_info_homepage_mid_success_${dt}.log
     33      33 homepage_mid_fail=publish_info_homepage_mid_fail_${dt}.log
     34      34 rm ${homepage_uid} ${homepage_mid_succ} ${homepage_mid_fail}
     35      35 for file in ${homepage[@]}
     36      36 do
     37      37     cat $file | grep SUCCESS -B1 | cut -d' ' -f 8 | cut -d $'\t' -f 2 | sort -u >> ${homepage_uid}
     38      38     cat $file | grep SUCCESS -B1 | cut -d' ' -f 8 | cut -d $'\t' -f 1 | sort -u >> ${homepage_mid_succ}
     39      39     cat $file | grep FAILURE -B1 | cut -d' ' -f 8 | cut -d $'\t' -f 1 | sort -u >> ${homepage_mid_fail}
     40      40 done
     41 t chujie
