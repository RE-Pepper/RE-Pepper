#pragma once

#include <Layout/alLayoutActor.h>

namespace al
{

class WipeSimple : public al::LayoutActor
{
        int _30;

public:
        void exeClose();
        void exeWait();
        void exeOpen();

        bool isCloseEnd() const;

public:
        virtual void appear();

public:
        WipeSimple( const char* name, const char* archive, const LayoutInitInfo& info, const char* suffix = nullptr );
};

} // namespace al
