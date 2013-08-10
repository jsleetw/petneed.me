package me.petneed.android.view;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.widget.StaggeredGridView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import me.petneed.android.R;
import me.petneed.android.model.AnimalListAdapter;
import me.petneed.android.model.DataManager;


public class SectionFragment extends Fragment implements DataManager.DataUpdatedListener {

    private AnimalListAdapter adapter;

    public void setDataManager(DataManager dataManager) {
        this.dataManager = dataManager;
    }

    public void setType(String type) {
        this.type = type;
    }

    private DataManager dataManager;
    private String type;
    /**
     * The fragment argument representing the section number for this
     * fragment.
     */
    public static final String ARG_SECTION_NUMBER = "section_number";
    public static final String ARG_TYPE = "type";

    public SectionFragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        type = (String)this.getArguments().get(ARG_TYPE);
        View rootView = inflater.inflate(R.layout.fragment_main_dummy,
                container, false);
        StaggeredGridView gridView = (StaggeredGridView) rootView.findViewById(R.id.section_grid_view);
        adapter = new AnimalListAdapter(dataManager, type);
        gridView.setAdapter(adapter);
        return rootView;
    }

    @Override
    public void dataUpdated(DataManager.ApiType code) {
        if (adapter != null){
            adapter.notifyDataSetChanged();
        }
    }

    @Override
    public void dataUpdateFailed(DataManager.ApiType code) {

    }

    @Override
    public void dataDetailView(Object obj) {

    }
}