# kol3btest_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# (test, [G  A  s  t],  hint)

  (0,[ [ [(1,3),(3,2)],[(0,3),(2,20)],[(1,20),(5,1),(3,6)],[(0,2),(2,6),(4,1)],[(3,1),(5,7)],[(4,7),(2,1)] ],[50,100,1,20,2,70],0,5],7),
  (1,[ [ [(1,3),(3,2)],[(0,3),(2,20)],[(1,20),(5,1),(3,6)],[(0,2),(2,6),(4,1)],[(3,1),(5,7)],[(4,7),(2,1)] ],[50,100,1,20,2,70],0,2],6),
  (2,[ [ [(1,3),(3,2)],[(0,3),(2,20)],[(1,20),(5,1),(3,6)],[(0,2),(2,6),(4,1)],[(3,1),(5,7)],[(4,7),(2,1)] ],[50,100,1,20,2,70],0,4],3),
  (3,[ [ [(1,3),(3,2)],[(0,3),(2,20)],[(1,20),(5,1),(3,6)],[(0,2),(2,6),(4,1)],[(3,1),(5,7)],[(4,7),(2,1)] ],[50,100,1,20,2,70],1,4],6),
  (4,[ [ [(1,3),(3,2)],[(0,3),(2,20)],[(1,20),(5,1),(3,6)],[(0,2),(2,6),(4,1)],[(3,1),(5,7)],[(4,7),(2,1)],[(7,10)],[(6,10),(8,20)],[(7,20)] ],[50,100,1,20,2,70,100,200,300],2,8],131),
  (5,[ [ [(1,3),(3,2)],[(0,3),(2,20)],[(1,20),(5,1),(3,6)],[(0,2),(2,6),(4,1)],[(3,1),(5,7)],[(4,7),(2,1)],[(7,10)],[(6,10),(8,20)],[(7,20)] ],[50,100,1,20,2,70,100,200,300],0,7],115),
  (1500,[],200),
  (2000,[],126),
  (3000,[],138),
  (5000,[],115),
]


from testy import MY_random

def my_randint(a,b):
  return a+MY_random()%(b-a+1)

def gentest(test, arg, hint ):
  if test<6:
    return arg,hint
  
  n = test
  e = 3*n
  t = set()
  G = [ [] for _ in range(n)]
  for _ in range(e):
    u = my_randint(0,n-1)    
    v = my_randint(0,n-1)    
    if u==v: continue
    if u>v: u,v = v,u
    if (u,v) in t: continue
    w = my_randint(10,99)
    t.add((u,v))
    G[u].append((v,w))
    G[v].append((u,w))
  
  A = [my_randint(20,200) for _ in range(n)]

  a = my_randint(0,n-1)   
  while True:
    b = my_randint(0,n-1)   
    if b!=a: break

  return [G,A,a,b],hint
   

  
