
def find_packet_signal(signal_length, star_text):

    with open("input.txt") as f:
        for line in f:
            chars = list(line)
            ch=[]
            for i_c in range(len(chars)):
                ch.append(chars[i_c])
                if len(ch) > signal_length:
                    ch = ch[-signal_length:]

                    identicals = 0
                    for i in range(len(ch)-1):
                        for j in range(i+1,len(ch)):
                            identicals += (ch[i] == ch[j])
                    
                    if identicals == 0:
                        print(f"Yes? {star_text}", i_c+1)
                        print(f"Signal: {i_c}", ch)
                        break
                
                #print(i_c, ch)
    return None

# Star 1:
find_packet_signal(4, "Star 1, a signal: ")

# Star 2:
find_packet_signal(14, "Star 2, signal boogaloo: ")


"""
#Initial chaos-solution:
#s1
with open("input.txt") as f:
    for line in f:
        chars = list(line)
        ch=[]
        for i_c in range(len(chars)):
            if len(ch) > 3:
                ch = ch[-3:]
                identicals = ch[0] != ch[1] and ch[0] != ch[2] and ch[1] != ch[2]
                if chars[i_c] not in ch and identicals:
                    print("Yes? Star 1:", i_c+1)
                    print(i_c, ch, chars[i_c])
                    break
            ch.append(chars[i_c])
            
#s2
with open("input.txt") as f:
    for line in f:
        chars = list(line)
        ch=[]
        for i_c in range(len(chars)):
            if len(ch) > 13:
                ch = ch[-13:]

                identicals = 0
                for i in range(len(ch)-1):
                    for j in range(i+1,len(ch)):
                        identicals += (ch[i] == ch[j])
                if chars[i_c] not in ch and identicals==0:
                    print("Yes? Star 2:", i_c+1)
                    print(i_c, ch, chars[i_c])
                    break
            ch.append(chars[i_c])
            print(i_c, ch)
"""