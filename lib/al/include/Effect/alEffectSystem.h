#pragma once

#include <heap/seadHeap.h>

namespace al
{

class EffectSystem
{
private:
        sead::Heap* _0;

public:
        void init();
        void startScene();

public:
        EffectSystem();
};

} // namespace al
