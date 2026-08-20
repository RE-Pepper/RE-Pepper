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
