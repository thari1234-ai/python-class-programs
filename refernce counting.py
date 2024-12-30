import sys
a=[1,2,3]
ref_count=sys.getrefcount(a)
print(ref_count)
#it tracks the num of references
import sys
a=[]
b=a
c=b
print(sys.getrefcount(a))
