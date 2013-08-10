package me.petneed.android.model;

import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import me.petneed.android.view.AnimalItemView;
import me.petneed.android.view.AnimalItemView_;

/**
 * Created by Jacob Chen on 8/10/13.
 */
public class AnimalListAdapter  extends BaseAdapter {

    private final DataManager dataManager;
    private String type;

    public AnimalListAdapter(DataManager _dataManager, String _type){
        dataManager = _dataManager;
        type = _type;
    }


    @Override
    public int getCount() {
        return dataManager.getDataByType(type).size();
    }

    @Override
    public Object getItem(int i) {
        return dataManager.getDataByType(type).get(i);
    }

    @Override
    public long getItemId(int i) {
        return dataManager.getDataByType(type).get(i).getAcceptNumValue();
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        AnimalItemView gv = null;
        //Log.d(TAG, "getView position " + position);
        final Animal item = (Animal) getItem(i);

        if (view == null) {
            gv = AnimalItemView_.build(dataManager.getContext());

            gv.setOnClickListener(new View.OnClickListener() {

                @Override
                public void onClick(View v) {
                    AnimalItemView aniView =  (AnimalItemView) v;
                    dataManager.getListener().dataDetailView(aniView.getItem());
                }

            });
        } else {
            gv = (AnimalItemView) view;
        }

        gv.bind(item);
        return gv;
    }
}
