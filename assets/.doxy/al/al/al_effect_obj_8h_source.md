

# File alEffectObj.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Npc**](dir_43489f5cd47c3c88012e1bbb9faf90cc.md) **>** [**alEffectObj.h**](al_effect_obj_8h.md)

[Go to the documentation of this file](al_effect_obj_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{

class EffectObj : public MapObjActor
{
        friend class EffectObjFunction;

private:
        sead::Matrix34f mBaseMtx;

public:
        virtual void                   init( const ActorInitInfo& info );
        virtual void                   makeActorAppeared();
        virtual void                   kill();
        virtual const sead::Matrix34f* getBaseMtx() const;
        virtual void                   control();

public:
        EffectObj( const sead::SafeString& name );
};

class EffectObjFunction
{
public:
        static void initActorEffectObj( EffectObj* actor, const ActorInitInfo& info, const char* objectName );
};

} // namespace al
```


