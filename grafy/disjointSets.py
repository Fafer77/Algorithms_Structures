def find(v, parent):
    if (parent[v] == v):
        return v
    else:
        return find(parent[v], parent)
 
def union(parent, u, v):
    u_par = find(u, parent)
    v_par = find(v, parent)
    parent[u_par] = v_par
