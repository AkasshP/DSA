class Solution {
    public Map<Integer,List<Integer>> map = new HashMap<>();
    public int visited;
    public Set<Integer> unionset = new HashSet<>();
    public List<Integer> temp = new ArrayList<>();
    public List<List<Integer>> cluster = new ArrayList<>();
    public int findCircleNum(int[][] isConnected) {
        visited = isConnected[0].length;
        int j = 0;
        for(int[] x: isConnected) 
        {
            temp.clear(); // reset
            for (int i = 0;i < x.length;i++)
            {
                if ((x[i] != 0) && (i != j)) temp.add(i);
            }
            map.put(j,new ArrayList(temp)); //update the list with node connection
            j++;
        }
        System.out.println(map);
        for (int i: map.keySet())
        { 
            temp.clear();
            if (!unionset.contains(i))
            {   
                dfs(i,temp);
                cluster.add(temp); //backtracking add the temp in cluster
            }
        }
    return cluster.size();
    }
    public void dfs(int src, List<Integer> temp)
    {
        if (unionset.contains(src) || unionset.size() == visited) return;
        else
        { 
            unionset.add(src);
            temp.add(src);//opening a group
        }
        for(int i : map.get(src))
        {
            dfs(i,temp);
        }
    }

}