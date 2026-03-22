

# File AquariumSwimDebris.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**MapObj**](dir_2096800ae80e9b320e335490a6d8aa70.md) **>** [**AquariumSwimDebris.h**](_aquarium_swim_debris_8h.md)

[Go to the documentation of this file](_aquarium_swim_debris_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

class AquariumSwimDebris : public al::MapObjActor
{
public:
        void exeAppear();

public:
        virtual void init( const al::ActorInitInfo& info );

public:
        AquariumSwimDebris( const sead::SafeString& name );
};
```


