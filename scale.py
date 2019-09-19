import pdb
from note import Note
class Scale():

    def __init__(self, pattern,note_id):
        self._pattern = pattern
        self._note_id = note_id
    
    
        
    
    def __str__(self):
        note_list = []
        note = Note(self._note_id)
        note_list.append(str(note))
        #pdb.set_trace()
        for ch in self._pattern:
            if ch  == 'W':
                note = note.whole(True)
            else:
                note = note.half(True)
            note_list.append(str(note))
        return str(note_list)
        
        


scale = Scale("WWHWWWW",11)
print(scale)