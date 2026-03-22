#pragma once

#include <Nerve/alHostStateBase.h>

#include "Sequence/ProductSequence.h"

namespace al
{
class LayoutInitInfo;
}
class WindowConfirmButton;
class WindowConfirmSingle;
class ProductStageStartParam;

class ProductStateTitle : public al::HostStateBase<ProductSequence>
{
private:
        ProductStageStartParam* mStartParam;
        WindowConfirmButton*    mButton;
        WindowConfirmSingle*    mWindow;
        void*                   _1C;
        void*                   _20;
        bool                    _24;
        bool                    _25;

public:
        ProductStateTitle( ProductSequence* host, ProductStageStartParam* startParam, const al::LayoutInitInfo& info );

        virtual void init();

        void exeLoad();
};
