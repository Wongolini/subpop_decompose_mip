import pandas as pd
import argparse
import re

def GetSamples(table):
    samples = []
    cols = table.columns
    for c in cols:
        try:
            x = re.search('[1-6][A-Z][1-9][1-9]',c)[0]
        except TypeError:
            try:
                x = re.search('[1-6][A-Z][1-9]',c)[0]
            except TypeError:
                try:
                    x = re.search('[1-6][A-Z]',c)[0]
                except TypeError:
                    continue
        if x is not None:
            samples.append(x)

    return samples

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',help='freq_sub_collapsed.tsv - output of decompose.py')
    parser.add_argument('-a',help='annotated table - output of subpop_naming.py')
    parser.add_argument('-v',help='original table - input to decompose.py')
    parser.add_argument('-o',help='outpath')
    args = parser.parse_args()
    if args.o[-1] !='/':
        args.o=args.o+'/'
    ann_df = pd.read_csv(args.a,sep='\t')
    sample_names = GetSamples(pd.read_csv(args.v,sep='\t'))
    freq_df = pd.read_csv(args.f, sep='\t',names=sample_names)
    out_df = pd.concat((freq_df,ann_df),axis=1)
    out_df.to_csv(args.o+'annotated_freq_sub_collapsed.tsv',sep='\t', index=False)
    print(out_df)
    
