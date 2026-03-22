#pragma once

#include <Layout/alLayoutActor.h>

class WindowConfirmButton : public al::LayoutActor
{
private:
        void* _30;

public:
        virtual void appear();

public:
        WindowConfirmButton( const char* name, const al::LayoutInitInfo& info );
};
