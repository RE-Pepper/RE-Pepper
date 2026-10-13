#pragma once

#include <Nerve/alHostStateBase.h>

#include "Sequence/ProductSequence.h"

namespace al
{
class LayoutInitInfo;
}

class ProductStateTitle : public al::HostStateBase<ProductSequence>
{
private:
        int                     _10;
        ProductStageStartParam* mStartParam;
        void*                   _18;
        void*                   _1C;
        void*                   _20;
        void*                   _24;
        void*                   _28;
        void*                   _2C;
        void*                   _30;
        void*                   _34;
        void*                   _38;
        void*                   _3C;

public:
        void set_10( int v )
        {
                _10 = v;
        }

public:
        ProductStateTitle( ProductSequence* host, ProductStageStartParam* startParam, const al::LayoutInitInfo& info );
};
