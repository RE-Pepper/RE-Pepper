#pragma once

#include <heap/seadHeap.h>

namespace al
{
class FunctorBase;

void createAndStartInitializeThread( sead::Heap* heap, int stackSize, const FunctorBase& func );

} // namespace al
