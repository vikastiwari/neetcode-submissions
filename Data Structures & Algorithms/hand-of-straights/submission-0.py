import collections

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Sanity Check: If the cards can't be divided evenly, it's impossible.
        if len(hand) % groupSize != 0:
            return False
            
        # Count all our cards
        count = collections.Counter(hand)
        
        # Sort the unique cards so we always look at the smallest available card first
        unique_cards = sorted(count.keys())
        
        for card in unique_cards:
            if count[card] > 0:
                # We MUST start 'needed' number of sequences with this card
                needed = count[card]
                
                # Check if we can build a valid sequence of length 'groupSize'
                for i in range(groupSize):
                    if count[card + i] < needed:
                        # We don't have enough cards to finish the sequence!
                        return False
                    
                    # Consume the cards
                    count[card + i] -= needed
                    
        return True
