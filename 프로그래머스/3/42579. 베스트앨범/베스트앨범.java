import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<>();
//         장르별로 play 수 더한 총 합 수.
        HashMap<String, Integer> total_play = new HashMap<>();
//         장르별로 또 하나의 HashMap으로 인덱스와 플레이 수 연결. 
        HashMap<String, HashMap<Integer,Integer>> genres_count = new HashMap<>();
        
        for (int i=0; i<plays.length; i++){
//             total_play에 장르가 포함되지 않았을 때.
            if(!total_play.containsKey(genres[i])){
//                 주어진 조건들 하나씩 추가.
                HashMap<Integer,Integer> count = new HashMap<>();
                count.put(i,plays[i]);
                genres_count.put(genres[i], count);
                total_play.put(genres[i], plays[i]);
            } else {
//                 total_play에 장르가 이미 존재할 때, play수 더함.
                total_play.put(genres[i], total_play.get(genres[i]) + plays[i]);
//                 장르별로 인덱스와 플레이 수 추가함.
                genres_count.get(genres[i]).put(i,plays[i]);
            }
            
        }
        // System.out.println(total_play); {pop=3100, classic=1450}
        // System.out.println(genres_count); {pop={1=600, 4=2500}, classic={0=500, 2=150, 3=800}}
        
//         Value값으로 내림차순 정렬하기 위해서 람다식 사용. 1) Key를 기준으로 리스트 만듦. 2) Collections.sort 와 람다식 사용하여 내림차순 정렬.
        List<String> keySet = new ArrayList<>(total_play.keySet());
        Collections.sort(keySet, (s1, s2) -> total_play.get(s2) - (total_play.get(s1)));
        
        
//         장르별 플레이 수도 내림차순 정렬하기.
        for (String key : keySet){
//             장르값(key)별로 value를 Hashmap만들기.
            HashMap<Integer, Integer> map = genres_count.get(key);
            
//             장르값 별로 가져온 map에 key값 추출.
            List<Integer> genres_key = new ArrayList(map.keySet());
            
//             장르키의 값을 기준으로 내림차순 정렬.
            Collections.sort(genres_key, (s1,s2) -> map.get(s2) - (map.get(s1)));

            
         answer.add(genres_key.get(0));
        if (genres_key.size() > 1){
            answer.add(genres_key.get(1));
        }
        }
        
              
        return answer.stream().mapToInt(i-> i).toArray();
    }
}