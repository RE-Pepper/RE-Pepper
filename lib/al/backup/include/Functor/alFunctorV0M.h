#pragma once

#include <Functor/alFunctorBase.h>

namespace al
{

template <typename T, typename F>
class FunctorV0M : public FunctorBase
{
private:
        T mParent;
        F mFuncPtr;

public:
        virtual void operator()() const
        {
                ( mParent->*mFuncPtr )();
        }

        virtual FunctorV0M* clone() const
        {
                return new FunctorV0M<T, F>( mParent, mFuncPtr );
        }

public:
        FunctorV0M( T parent, F funcPtr ) : mFuncPtr( funcPtr ), mParent( parent )
        {
        }
};

} // namespace al
