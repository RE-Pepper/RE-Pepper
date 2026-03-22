#pragma once

#include <Layout/alLayoutActor.h>

namespace al
{
class LayoutInitInfo;
}

class GameCountUp : public al::LayoutActor
{
private:
        sead::Vector3f _30;
        bool           _3C;

public:
        GameCountUp( const al::LayoutInitInfo& info );
};
