# HITS

HITS(Hyperlink-Induced Topic Search)はJon Kleinbergが開発したWebページを評価するアルゴリズムです．

## 参考リンク

- [Kleinberg, J. M. (1997). Authoritative Sources in a Hyperlinked Environment .](https://www.cs.cornell.edu/home/kleinber/auth.pdf)
- [Wikipedia[en]「HITS algorithm」](https://en.wikipedia.org/wiki/HITS_algorithm#cite_note-1)
- [Web Data Mining: Exploring Hyperlinks, Contents, and Usage Data (Data-Centric Systems and Applications)](https://www.amazon.co.jp/Web-Data-Mining-Data-Centric-Applications/dp/3642194591)
- [naoyaのはてなダイアリー「HITS, 主成分分析, SVD」](https://naoya-2.hatenadiary.org/entry/20090301/hits)
- [マイムの部屋「HITSアルゴリズム」](http://mimuuow.hatenablog.com/entry/2015/10/28/113539)
- [networkx「hits」](https://networkx.github.io/documentation/networkx-1.9.1/reference/generated/networkx.algorithms.link_analysis.hits_alg.hits.html)
- [GeeksforGeeks「Hyperlink Induced Topic Search (HITS) Algorithm using Networxx Module | Python」](https://www.geeksforgeeks.org/hyperlink-induced-topic-search-hits-algorithm-using-networxx-module-python/)

## Environment

- Python 3.7.3
  - matplotlib                         3.1.0
  - networkx                           2.3
  - pprint                             0.1

## Sampleネットワーク

![sampleDigraph](img/sample_digraph.png)

Network xでの実行結果(iter=60,normalize=true)

```
'Authority Scores'
{'A': 0.12259059198121637,
 'B': 0.15938748867805191,
 'C': 0.33351811426192646,
 'D': 0.15938748867805191,
 'E': 0.06773750229574053,
 'F': 0.13248067440906394,
 'G': 0.0,
 'H': 0.02489813969594891}

'Hub Scores'
{'A': 0.062151232534615714,
 'B': 0.1564647974400908,
 'C': 0.05751145547702772,
 'D': 0.13005137383066068,
 'E': 0.30601308310927944,
 'F': 0.062151232534615714,
 'G': 0.17785409945218528,
 'H': 0.04780272562152461}
```

## Note

![IMG1](img/hits.png)
![IMG2](img/hitss.png)
![IMG3](img/hitsss.png)
![IMG4](img/hitssss.png)
