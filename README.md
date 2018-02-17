## NLU project

### Set up Git

Project team only. Follow the steps as described in [this article](https://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/).

### Download data sets

In the repository directory, run the following commands to download the data, clean up hidden files, and unzip:

```
$ cd data/

$ curl -O https://nlp.stanford.edu/projects/snli/snli_1.0.zip
$ zip -d snli_1.0.zip __MACOSX/\*
$ zip -d snli_1.0.zip \*/.DS_Store
$ unzip snli_1.0.zip

$ curl -O https://www.nyu.edu/projects/bowman/multinli/multinli_1.0.zip
$ zip -d multinli_1.0.zip __MACOSX/\*
$ zip -d multinli_1.0.zip \*/.DS_Store
$ unzip multinli_1.0.zip
```

Alternatively, [download the updated data folder here](https://www.dropbox.com/sh/rjx2z98a10fz1li/AAAIM9ubvBT9i8a7sIOA9TNIa?dl=0).


### Run

#### Set up a virtual environment and install requirements

```
$ git clone https://github.com/melanietosik/nlu-project
$ cd nlu-project/
$ virtualenv -p python3 env/
$ source env/bin/activate
$ pip install -r requirements.txt
$ python -m spacy download en
```

#### Scripts

##### Split data into quantifier pairs/other

```
$ python scripts/split_data.py data/snli_1.0/snli_1.0_train.jsonl
#quant pairs: 17136
#other pairs: 533016
```

```
$ python scripts/split_data.py data/snli_1.0/snli_1.0_dev.jsonl
#quant pairs: 303
#other pairs: 9697
```

```
$ python scripts/split_data.py data/snli_1.0/snli_1.0_test.jsonl
#quant pairs: 295
#other pairs: 9705
```

```
$ python scripts/split_data.py data/multinli_1.0/multinli_1.0_train.jsonl
#quant pairs: 18235
#other pairs: 374467
```

```
$ python scripts/split_data.py data/multinli_1.0/multinli_1.0_dev_matched.jsonl
#quant pairs: 475
#other pairs: 9525
```

```
$ python scripts/split_data.py data/multinli_1.0/multinli_1.0_dev_mismatched.jsonl
#quant pairs: 448
#other pairs: 9552
```
