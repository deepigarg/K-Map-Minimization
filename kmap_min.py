# CSE 101 - IP HW2
# K-Map Minimization 
# Name: DEEPI GARG
# Roll Number: 2018389
# Section: B
# Group: 6
# Date: 12-10-2018

def minFunc(numVar, stringIn):
        """
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.
        Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
        Output is a string representing the simplified Boolean Expression in
        SOP form.

        No need for checking of invalid inputs.
        
        Do not include any print statements in the function.
        """
        
        d = stringIn.find('d') # to find the index of 'd'
        if d==0:
                mint=''
        else:
                mint=stringIn[1:d-1]
                
        if mint=='':
                print(0)
                return 0  # if no minterms, then function is always 0
        else:
                mint=mint.split(',')
                mint=list(map(int,mint))  #list of ones

        if stringIn[d+1]=='-':
                dont=['']
        else:
                dont=stringIn[d+2:-1]
                dont=dont.split(',')

        if dont==['']:
                dont=[]
        else:
                dont=list(map(int,dont))  #list of don't - cares

        ones=[]  #list of ones and don't - cares (all minterms)
        minones=[]  #list of corresponding decimal repsresentation of minterms
        
        for i in mint+dont:
                minones.append(i)
        minones.sort() #appended all decimal representaion of minterms in sorted order

        one=False
        for i in range(2**numVar):
                if i in minones:
                        one=True
                else:
                        one=False
                        break
        if one==True:
                print(1)
                return 1   # if all numbers are there as either minterms or don't-cares, then function is always 1


        for i in minones:
                q=i
                bi=''
                while q!=0:
                        bi=str(q%2) + bi 
                        q=q//2
                if len(bi)<numVar:
                        for a in range(numVar-len(bi)):
                                bi='0'+bi
                # converted the binary no. to the correct number of bits
                ones.append(bi)  # final list of all the minterms in binary format

        mint=list(map(str,mint))
        dont=list(map(str,dont))
        minones=list(map(str,minones))
        
        g1=[]
        ming1=[]
        for i in range(numVar+1):
                g1.append([])
                ming1.append([])

        for i in range(len(ones)):
                for j in range(0,5):
                        if ones[i].count("1")==j:
                                g1[j].append(ones[i])  # grouping the minterms with respect to number of 1's in the binary representation
                                ming1[j].append(minones[i]) # corresponding groups with decimal represntation



        pi=[]  #list of prime implicants
        used=[]
        minpi=[]  # decimal representation of respective pi's
        used_m=[]
        
        while (g1[0]!=[] or g1[1]!=[] or g1[2]!=[] or g1[-1]!=[] or g1[-2]!=[]):
                gcom1=[]
                mingcom1=[]
                for i in range(len(g1)):
                        gcom1.append([])
                        mingcom1.append([])

                        ind_j=-1
                        for j in g1[i]:
                                ind_j = ind_j + 1
                                if len(g1)!=i+1:

                                        ind_k=-1
                                        for k in g1[i+1]:
                                                ind_k = ind_k + 1
                                                com=0
                                                comind=0

                                                for z in range(numVar):
                                                        if j[z]!=k[z]:
                                                                com=com+1
                                                                comind=z
                                                if com==1:
                                                        gcom1[i].append(j[:comind]+"-"+j[comind+1:])
                                                        mingcom1[i].append(str(ming1[i][ind_j])+'-'+str(ming1[i+1][ind_k]))
                                                        used.append(j)
                                                        used.append(k)
                                                        used_m.append(ming1[i][ind_j])
                                                        used_m.append(ming1[i+1][ind_k])
                for i in range(len(g1)):
                        for j in g1[i]:
                                if j not in used:
                                        pi.append(j)
                
                for i in range(len(ming1)):
                        for j in ming1[i]:
                                if j not in used_m:
                                        minpi.append(j)

                g1=gcom1
                ming1=mingcom1

                
        
        for i in range(len(pi)):
                for j in range(i+1,len(pi)):
                        if pi[i]==pi[j]:
                                pi[j]=''
                                minpi[j]=''
        # redundant terms from the prime-implicant list and the corresponding minterm list have been removed
                
        pil=[]  # this list contains the prime implicants in terms of variables
        for i in pi:
                a=''
                if i!='':
                        
                        if i[0]=='0':
                                a = a + "W'"
                        elif i[0]=='1':
                                a = a + "W"
                        if i[1]=='0':
                                a = a + "X'"
                        elif i[1]=='1':
                                a = a + "X"
                        if numVar>=3:
                                if i[2]=='0':
                                        a = a + "Y'"
                                elif i[2]=='1':
                                        a = a + "Y"
                                if numVar==4:
                                        if i[3]=='0':
                                                a = a + "Z'"
                                        elif i[3]=='1':
                                                a = a + "Z"
                        pil.append(a)
                else:
                        pil.append('')
        

                        
        minpi_l=[]  # list of decimal numbers covered by respective minterms
        for i in minpi:
                minpi_l.append(i.split('-'))

        

        table={}  # dictionary of decimal number as key and corresponing minterms as data
        for i in mint:
                i=str(i)
                table[i]=[]
                
                for j in minpi_l:
                        if i in j:
                                table[i].append(j)
        
        dont=list(map(str,dont))
        for i in range(len(minpi_l)):
                for j in range(len(minpi_l[i])):
                        if minpi_l[i][j] in dont:
                                minpi_l[i][j]=''
        # removed the don't-care numbers from list
                
                                                             
                                        
        expr=[]
        for i in table:
                if len(table[i])==1:
                        sure=table[i][0]
                        for q in range(len(pil)):
                                if minpi_l[q]==table[i][0]:

                                        if pil[q] not in expr:
                                                expr.append(pil[q])
        # appended the essential prime implicants in a list
                

        for i in range(len(minpi_l)):
                if minpi_l[i]!=['']:
                        l=0
                        for j in range(len(minpi_l[i])):
                                if minpi_l[i][j]!='':
                                        l=l+1
                                        n=minpi_l[i][j]
                                        num=j
                        if l==1:
                                for k in range(len(minpi_l)):
                                        for m in range(len(minpi_l[k])):
                                                if k!=i and n==minpi_l[k][m]:
                                                        pil[i]=''
                                                        minpi_l[i][num]=''
                        elif l==0:
                                pil[i]=''
                                minpi_l[i][num]=''
                        # removed terms which cover only don't care ones and already covered ones

                        
        
        
        for i in mint:    # mint is the list of minterms without the don't cares 
                count=0
                for j in range(len(minpi_l)):
                        for k in minpi_l[j]:
                                if i==k:
                                        count=count+1
                                        n=j
                if count==1:
                        if pil[n] not in expr:
                                expr.append(pil[n])  # appended those terms to the final expression list, which cover ones that are not covered by any other term


        covered=[]
        for i in range(len(pil)):
                if pil[i] in expr:
                        for j in minpi_l[i]:
                                covered.append(j)  # made a list which contains those ones which have been covered
                                
        for i in mint:
                br=0
                if i not in covered:
                        for j in range(len(minpi_l)):
                                for k in minpi_l[j]:
                                        if i==k :
                                                if pil[j] not in expr:
                                                        expr.append(pil[j])  #appended the term containing the not-covered minterms in the final list
                                                        br=1
                                                        break
                                                        covered.append(i)
                                if br==1:
                                        break

        
        for i in range(len(expr)):
                for j in  range(len(pil)):
                        if expr[i]==pil[j]:
                                repl=[]
                                for k in minpi_l[j]:
                                        rep=False       
                                        for l in range(len(minpi_l)):
                                                if j!=l and pil[l] in expr and k!='':
                                                        if k in minpi_l[l]:
                                                                rep=True
                                                                break
                                                        else:
                                                                rep=False
                                                elif k=='':
                                                        rep=True
                                                                
                                        if rep==True:
                                                repl.append(True)
                                        else:
                                                repl.append(False)
                                if False not in repl:
                                        expr[i]=''
                                        
        # removed those terms from the final list, which cover already covered terms


                                        
        expr.sort() # sorting lexicographically
        out=''
        for i in expr:
                if out=='':
                        out=out+i
                else:
                        out=out+'+'+i
                # final output


        print("minterms:",mint)
        print("Don't cares:",dont)
        print("OUTPUT=",out)

        return(out)
	

	
