

# File BlockDragonGenerator.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Enemy**](dir_e35196509c323c9bb4cd921cf1b24d53.md) **>** [**BlockDragonGenerator.h**](_block_dragon_generator_8h.md)

[Go to the documentation of this file](_block_dragon_generator_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

class BlockDragonGenerator : public al::MapObjActor
{
private:
        u8 _60[ 0x60 ];

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void startClipped();
        virtual void endClipped();

public:
        BlockDragonGenerator( const sead::SafeString& name );
};
```


