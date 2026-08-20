#pragma once

#include <stddef.h>

namespace al
{

class LiveActor;

class ExecuteRequestKeeper
{
private:
        u8 _0[ 0x10 ];

public:
        void request( LiveActor*, int );

public:
        ExecuteRequestKeeper( size_t );
};

} // namespace al
