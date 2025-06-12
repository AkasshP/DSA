class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cards = {}
        temp_deck = []
        visited = []
        if hand:
            if groupSize == 1:
                return True     
        else:
            return False

        for i in hand:
            if cards.get(i):
                cards[i] = cards[i] + 1
            else:
                cards[i] = 1

        def shuffle(cards):
            if cards:
                for i in sorted(cards):
                    if len(temp_deck) != groupSize: #(if set is not full then try to add)
                        if temp_deck:
                            if temp_deck[-1] + 1 == i:
                                temp_deck.append(i)
                                if cards.get(i):
                                    cards[i] = cards[i] - 1
                                    if cards[i] == 0:
                                        del cards[i] #so that new sorted card comes first

                        else:
                            temp_deck.append(i) 
                            if cards.get(i):
                                cards[i] = cards[i] - 1
                                if cards[i] == 0:
                                    del cards[i]
                            
                    else: #set is full then reset and shuffle again
                        visited.append(tuple(sorted(temp_deck)))
                        temp_deck.clear() #resetting
                        if shuffle(cards):
                            return True

                #cards are available and added in deck, but unvisited
                if not visited:
                    if cards:
                        if temp_deck:
                            if len(temp_deck) == groupSize:
                                visited.append(tuple(sorted(temp_deck)))   
                                temp_deck.clear() #resetting
                                if shuffle(cards):
                                    return True
                            else:
                                return False
                    else:
                        if len(temp_deck) == groupSize:
                            visited.append(tuple(sorted(temp_deck))) 
                            if len(visited) * groupSize == len(hand):
                                 return True 
                
                else:
                    if not cards:
                        if len(temp_deck) == groupSize:
                            visited.append(tuple(sorted(temp_deck))) 
                            if len(visited) * groupSize == len(hand):
                                return True 
                        
            else:
                if len(visited) * groupSize == len(hand):
                    return True    

            return False
        return shuffle(cards)
                

            

        
                
            
            
