

# File alActorFactory.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Factory**](dir_3f8e9df3dfd35c77b73e3e3b5744b002.md) **>** [**alActorFactory.h**](al_actor_factory_8h.md)

[Go to the documentation of this file](al_actor_factory_8h.md)


```C++
#pragma once

#include <Factory/alFactory.h>
#include <LiveActor/alLiveActor.h>

namespace al
{
class Resource;
class ByamlIter;

typedef CreateFuncPtr<LiveActor>::Type    CreateActorFuncPtr;
typedef NameToCreator<CreateActorFuncPtr> NameToActorCreator;

class ActorFactory
{
private:
        Resource*  mArchive;
        ByamlIter* mConvertNameData;

public:
        const char*        convertName( const char* objectName ) const;
        CreateActorFuncPtr getCreator( const char* objectName ) const;

public:
        ActorFactory();
};

} // namespace al
```


