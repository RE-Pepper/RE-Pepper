#pragma once

#include <Functor/alFunctorBase.h>

namespace al
{

class ExecuteRequestKeeper;
class ExecuteTableHolderDraw;
class ExecuteTableHolderUpdate;

class IUseExecutor
{
public:
        virtual void execute()
        {
        }

        virtual void draw()
        {
        }
};

class ExecuteDirector
{
        friend class LayoutKit;

private:
        size_t                    _0;
        ExecuteTableHolderUpdate* mUpdateTable;
        int                       mDrawTableAmount;
        ExecuteTableHolderDraw**  mDrawTables;
        ExecuteRequestKeeper*     mRequestKeeper;
        void*                     _14;
        void*                     _18;

public:
        void init();
        void createExecutorListTable();
        void registerUser( al::IUseExecutor* p, const char* str );
        void registerFunctor( const al::FunctorBase& base, const char* str );
        void registerFunctorDraw( const al::FunctorBase& base, const char* str );

public:
        ExecuteDirector( int );
};

} // namespace al
