import yaml

conf_string = '''
dataset:
  dir: "../input/data-science-bowl-2019/"
  feature_dir: "features"
  params:

features:
  - PastSummary3
  - NakamaV8

av:
  split_params:
    n_splits: 5
    random_state: 42

  model_params:
    objective: "binary"
    metric: "auc"
    boosting: "gbdt"
    max_depth: 7
    num_leaves: 75
    learning_rate: 0.01
    colsample_bytree: 0.7
    subsample: 0.1
    subsample_freq: 1
    seed: 111
    feature_fraction_seed: 111
    drop_seed: 111
    verbose: -1
    n_jobs: -1
    first_metric_only: True

  train_params:
    num_boost_round: 50000
    early_stopping_rounds: 200
    verbose_eval: 200

model:
  name: "mlp"
  mode: "ovr"
  save_path: "pth/"
  policy: "best_score"

  model_params:
    emb_drop: 0.3
    drop: 0.5

  train_params:
    batch_size: 256
    n_epochs: 50
    lr: 0.001
    scheduler:
      name: "cosine"
      T_max: 10
      eta_min: 0.00001

post_process:
  params:
    reverse: False
    n_overall: 20
    n_classwise: 20

val:
  name: "group_kfold"
  n_delete: 0.9
  percentile: 60
  params:
    n_splits: 5
    random_state: 111

output_dir: "output"
'''

config = dict(yaml.load(conf_string, Loader=yaml.SafeLoader))

params = config["val"]["params"]
kf = KFold(
    n_splits=params["n_splits"],
    random_state=params["random_state"],
    shuffle=True)

