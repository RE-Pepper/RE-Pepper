#pragma once

#include <Execute/alExecuteDirector.h>

namespace al
{

class LiveActor;

void registerExecutorUser( IUseExecutor* p, const char* name );
void registerExecutorFunctor( const FunctorBase& base, const char* name );
void registerExecutorFunctorDraw( const FunctorBase& base, const char* name );

} // namespace al

namespace alActorSystemFunction
{

void addToExecutorMovement( al::LiveActor* actor );
void removeFromExecutorDraw( al::LiveActor* actor );

} // namespace alActorSystemFunction
