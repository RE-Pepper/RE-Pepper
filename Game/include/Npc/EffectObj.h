#pragma once

#include <MapObj/alMapObjActor.h>



class EffectObj : public al::MapObjActor
{
        friend class EffectObjFunction;

private:
        sead::Matrix34f mBaseMtx;

public:
        virtual void                   init( const al::ActorInitInfo& info );
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
        static void initActorEffectObj( EffectObj* actor, const al::ActorInitInfo& info, const char* objectName );
};
