

# File NoteObj.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**MapObj**](dir_2096800ae80e9b320e335490a6d8aa70.md) **>** [**NoteObj.h**](_note_obj_8h.md)

[Go to the documentation of this file](_note_obj_8h.md)


```C++
#pragma once

#include "MapObj/NoteObjGenerator.h"

class NoteObj : public al::MapObjActor
{
private:
        sead::Quatf       mStartQuat;
        bool              _70;
        bool              _71;
        int               _74;
        sead::Vector3f    _78;
        NoteObjGenerator* mGenerator;

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void initAfterPlacement();
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );
        virtual void control();

public:
        NoteObj( const char* name );
        NoteObj( NoteObjGenerator* generator );
};
```


