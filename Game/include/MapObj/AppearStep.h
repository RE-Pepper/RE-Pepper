#pragma once

#include <MapObj/alMapObjActor.h>

class AppearStep : public al::MapObjActor
{
public:
        void exeAppear();
        void exeWait();
        void exeDisappear();
        void exeEnd();

public:
        virtual void init( const al::ActorInitInfo& info );

private:
        void startAppear();
        void startDisappear();

public:
        AppearStep( const sead::SafeString& name );
};
