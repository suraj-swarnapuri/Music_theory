
class Note():
    """
    represents the atomic unit for music
    id: c=1 d =2 e =3 f =4 g =5 a=6 b=7
    """

    def __init__(self,note_id):
        if note_id ==-1:
            self._id = 11
        elif note_id ==0:
            self._id = 12
        else:
            self._id = note_id % 12
            
        self._id = note_id
    def getName(self):
        name_map = {
            1: 'C',
            2: 'C#',
            3: 'D',
            4: 'D#',
            5: 'E',
            6: 'F',
            7: 'F#',
            8: 'G',
            9: 'G#',
            10: 'A',
            11: 'A#',
            12: 'B'
        }
        return name_map[self._id]

    def __str__(self):
        return "%s" % self.getName()
    
    def whole(self, up):
        """
        returns the note a whole step 
        param: bool UP - direction in which to  go
        """
        if up:
            return Note(self._id+2)
        return Note(self._id-2)

    def half(self, up):
        """
        returns the note a half step 
        param: bool UP - direction in which to  go
        """
        if up:
            return Note(self._id+1)
        return Note(self._id-1)

def main():
    c = Note(1)
    print(c)
    d = c.whole(True)
    print(d)
    cc = d.half(False)
    print(cc)

if __name__ == "__main__":
    main()

            

        


        

