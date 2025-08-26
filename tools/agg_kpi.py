#!/usr/bin/env python3
import csv, os, collections
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
INFILE = os.path.join(REPO, _data/csv/kpi_facts_weekly.csv)
OUTDIR = os.path.join(REPO, reports/out)
os.makedirs(OUTDIR, exist_ok=True)
AggKey = collections.namedtuple(AggKey, week