#pragma once

#include <Functor/alFunctorBase.h>

namespace al
{

class FunctorV0F : public FunctorBase
{
private:
        typedef void ( *FuncType )();
        FuncType mFuncPtr;

public:
        virtual void operator()() const
        {
                mFuncPtr();
        }

        virtual FunctorBase* clone() const
        {
                return new FunctorV0F( mFuncPtr );
        }

public:
        FunctorV0F( FuncType func ) : mFuncPtr( func )
        {
        }
};

} // namespace al
