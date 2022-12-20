class Solution {
    private boolean[] opened;
    public void go(List<List<Integer>> rooms,int index){
        opened[index] = true;
        for(int i : rooms.get(index)){
            if(opened[i]==true) continue;
            go(rooms,i);
        }
    }
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        this.opened = new boolean[rooms.size()];
        opened[0] = true;
        go(rooms,0);
        for(boolean b : opened) if (b==false) return b;
        return true;
    }
}