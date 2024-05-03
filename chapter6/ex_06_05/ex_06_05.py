text = "X-DSPAM-Confidence:    0.8475"

colon_pos = text.find(":")+1

n = float(text[colon_pos:].strip())

print(n)
