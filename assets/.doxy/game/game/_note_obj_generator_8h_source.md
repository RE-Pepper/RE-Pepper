

# File NoteObjGenerator.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**MapObj**](dir_2096800ae80e9b320e335490a6d8aa70.md) **>** [**NoteObjGenerator.h**](_note_obj_generator_8h.md)

[Go to the documentation of this file](_note_obj_generator_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{
class LiveActorGroup;
}

class NoteObjGenerator : public al::MapObjActor
{
private:
        al::LiveActorGroup* mNoteObjGroup;
        void*               _64;
        float               _68;
        float               _6C;
        void*               _70;
        int                 _74;
        bool                _78;
        float               _7C;
        void*               _80;
        bool                _84;

public:
        void exeWait();
        void exeMove();
        void exeDisappear();
        void exeSuccess();

public:
        NoteObjGenerator( const sead::SafeString& name );
};
```


