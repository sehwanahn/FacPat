import os,random,argparse,sys
import numpy as np
import pandas as pd

max_round = 200
stop_score = 0

no_generation = 100
no_fitness = 20
no_mating = (no_generation - no_fitness)/2      # no_fitness + no_mating*2 = no_generation
ratio_crossover = .7
ratio_doubleCrossover = .7
ratio_mutate = 0.7



def fitness(pattern,individual):
    col = np.array(individual[0])
    row = np.array(individual[1])
    row = np.reshape(row,(len(row),1))
    fit_dist = 0
    
    tmp_matrix = np.bitwise_or(col,row)
    fit_dist = np.sum(abs(pattern-tmp_matrix))
	
    return fit_dist
def mating(a, b,n_row,n_col):
    if random.randint(0,100) < ratio_crossover * 100:
        if random.randint(0,1) == 1:
            st1 = random.randint(0,n_row)
            st2 = random.randint(0,n_row)
            if abs(st1-st2) < 2:
                tmp = [a[0], a[1][0:st1] + b[1][st1:]]
                b =   [b[0], b[1][0:st1] + a[1][st1:]]
                a =   tmp
            else:
                tmp = [a[0], a[1][0:min(st1,st2)] + b[1][min(st1,st2):max(st1,st2)] + a[1][max(st1,st2):]]
                b =   [b[0], b[1][0:min(st1,st2)] + a[1][min(st1,st2):max(st1,st2)] + b[1][max(st1,st2):]]
                a = tmp
            if random.randint(0,100) < ratio_doubleCrossover * 100:
                st1 = random.randint(0,n_col)
                st2 = random.randint(0,n_col)
                if abs(st1-st2) < 2:
                    tmp = [a[0][0:st1] + b[0][st1:], a[1]]
                    b =   [b[0][0:st1] + a[0][st1:], b[1]]
                    a = tmp
                else:
                    tmp = [a[0][0:min(st1,st2)] + b[0][min(st1,st2):max(st1,st2)] + a[0][max(st1,st2):], a[1]]
                    b =   [b[0][0:min(st1,st2)] + a[0][min(st1,st2):max(st1,st2)] + b[0][max(st1,st2):], b[1]]
                    a = tmp
        else:
            st1 = random.randint(0,n_col)
            st2 = random.randint(0,n_col)
            if abs(st1-st2) < 2:
                tmp = [a[0][0:st1] + b[0][st1:], a[1]]
                b =   [b[0][0:st1] + a[0][st1:], b[1]]
                a = tmp
            else:
                tmp = [a[0][0:min(st1,st2)] + b[0][min(st1,st2):max(st1,st2)] + a[0][max(st1,st2):], a[1]]
                b =   [b[0][0:min(st1,st2)] + a[0][min(st1,st2):max(st1,st2)] + b[0][max(st1,st2):], b[1]]
                a = tmp
            if random.randint(0,100) < ratio_doubleCrossover * 100:
                st1 = random.randint(0,n_row)
                st2 = random.randint(0,n_row)
                if abs(st1-st2) < 2:
                    tmp = [a[0], a[1][0:st1] + b[1][st1:]]
                    b =   [b[0], b[1][0:st1] + a[1][st1:]]
                    a = tmp
                else:
                    tmp = [a[0], a[1][0:min(st1,st2)] + b[1][min(st1,st2):max(st1,st2)] + a[1][max(st1,st2):]]
                    b =   [b[0], b[1][0:min(st1,st2)] + a[1][min(st1,st2):max(st1,st2)] + b[1][max(st1,st2):]]
                    a = tmp
        return [a,b]
    else:
        return [[a[0],b[1]], [b[0],a[1]]]

def mutate(individual,n_row,n_col):
    mut_idx = random.randint(0, n_row + n_col - 1)
    if mut_idx >= n_col:
            return [individual[0], individual[1][0:(mut_idx - n_col)] + [abs(individual[1][mut_idx - n_col]-1)] + individual[1][(mut_idx - n_col + 1):]]
    else:
            return [individual[0][0:mut_idx] + [abs(individual[0][mut_idx]-1)] + individual[0][mut_idx + 1:], individual[1]]

def GA(pattern,outfile):
    n_row = np.shape(pattern)[0]
    n_col = np.shape(pattern)[1]

    popul = []
    ##### initial population #####
    for i in range(0,no_generation):
        xChr=yChr= []
        for j in range(0,n_col): xChr = xChr + [random.randint(0,1)]
        for j in range(0,n_row): yChr = yChr + [random.randint(0,1)]
        popul  = popul + [[xChr, yChr]]

    newPopul = popul

    outfile = open(outfile,'w')
    ##### fitness, select, mating, crossover, mutation #####
    for gen in range(max_round):
        fittest_list = []
        for i in range(len(newPopul)):
            fittest_list.append([fitness(pattern,newPopul[i]),i])
        ##### select parents #####
        fittest_list.sort()

        parents = []    ## Top fittest individuals
        for i in range(no_fitness):
            parents.append(newPopul[fittest_list[i][1]])

        distance = fittest_list[0][0]
        FSGP_col = parents[0][0]
        FSGP_row = parents[0][1]

        outfile.write("Round " + str(gen) + " => " + str(distance) + " : " + str(FSGP_col) + " , " + str(FSGP_row) + "\n")
        #print("Round " + str(gen) + " => " + str(distance) + " : " + str(FSGP_col) + " , " + str(FSGP_row))

        if distance <= stop_score or gen == max_round-1:
            break

        newPopul = parents
        ##### Mate and Crossover #####
        for i in range(0, int(no_mating)):
            x = newPopul[random.randint(0,len(newPopul)-1)]
            y = newPopul[random.randint(0,len(newPopul)-1)]
            children = mating(x,y,n_row,n_col)
            newPopul = newPopul + [children[0]] + [children[1]]
        for i in range(0, len(newPopul)):
            if random.randint(0,100) < ratio_mutate * 100:
                newPopul[i] = mutate(newPopul[i],n_row,n_col)
    outfile.close()

    return [distance,[FSGP_col,FSGP_row]]

def read_data(infile,th,outfile):
    df = pd.read_csv(infile,header=0,sep="\t")
    cols = df.columns[1:]
    rows = df[df.columns[0]]
    pattern = np.array(pd.DataFrame(df,columns=cols))

    condition = abs(pattern) >= th
    pattern[condition] = 1
    pattern[~condition] = 0

    result = GA(pattern,outfile)

    return result,list(cols),list(rows)


def main():
    parser = argparse.ArgumentParser(description="FacPat")
    parser.add_argument("-i",type=str,dest="input",help="Input file (tab-delimited)",required=True)
    parser.add_argument("-t",type=float,dest="threshold",help="Absolute threshold of Z-scores to make binary (default : |2|)",default=2.0)
    parser.add_argument("-o",type=str,dest="output",help="Output filename prefix",required=True,default="output.txt")
    args = parser.parse_args() 
    
    FacPat = read_data(args.input,args.threshold,args.output)
    
    Distance = FacPat[0][0]
    
    rows = []
    cols = []

    for i in range(0,len(FacPat[0][1][0])):
        if FacPat[0][1][0][i]==1:
            cols.append(FacPat[1][i])
    for i in range(0,len(FacPat[0][1][1])):
        if FacPat[0][1][1][i]==1:
            rows.append(FacPat[2][i])

    if len(rows)==0 and len(cols)==0:
        print("Distance : " + str(Distance))
        print("Pattern : Null")
    else: 
        print("Distance : " + str(Distance))
        print("Pattern : " + ",".join(cols) + "," + ",".join(rows))


if __name__ == "__main__":
    main()
    
    parser = argparse.ArgumentParser()

