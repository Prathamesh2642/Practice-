def largestAltitude(gain):
        netgain=[0]
        for i in gain:
            for j in netgain:
                temp=i+j
            netgain.append(temp)
        max=netgain[0]
        for i in netgain:
            if i>max:
                max=i
        return max    

        
