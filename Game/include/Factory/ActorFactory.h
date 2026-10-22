#pragma once

#include <Factory/alFactory.h>
#include <LiveActor/alLiveActor.h>

namespace al
{
class Resource;
class ByamlIter;
}

typedef al::CreateFuncPtr<al::LiveActor>::Type    CreateActorFuncPtr;
typedef al::NameToCreator<CreateActorFuncPtr>     NameToActorCreator;

class ActorFactory
{
private:
        al::Resource*  mArchive;
        al::ByamlIter* mConvertNameData;

public:
        const char*        convertName( const char* objectName ) const;
        CreateActorFuncPtr getCreator( const char* objectName ) const;

public:
        ActorFactory();
};
